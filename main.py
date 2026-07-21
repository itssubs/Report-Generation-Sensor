import argparse
import schedule
import time
from pipeline import SensorPipeline

def main():
    parser = argparse.ArgumentParser(description="Sensor Pipeline - Hourly & Monthly Reports")
    parser.add_argument('--mode', '-m', choices=['hourly', 'monthly'], default='monthly',
                        help='Execution mode')
    parser.add_argument('--input', '-i', default='Hourly Data check/Data',
                        help='Input data directory')
    parser.add_argument('--output', '-o', default='Hourly Data check/report',
                        help='Output directory')
    parser.add_argument('--interval', '-int', type=int, default=60,
                        help='Run interval in minutes (for hourly mode)')
    parser.add_argument('--dry', action='store_true', help='Dry run (no file output)')

    args = parser.parse_args()

    pipeline = SensorPipeline(input_dir=args.input, output_dir=args.output, mode=args.mode)

    if args.dry:
        print("🔍 DRY RUN MODE")
        if args.mode == "hourly":
            pipeline._load_clean_hourly()
        else:
            pipeline._load_clean_monthly()
        print("First 5 rows:\n", pipeline._data.head())
        return

    if args.mode == "hourly":
        # First immediate run
        pipeline.run()

        # Schedule recurring runs
        schedule.every(args.interval).minutes.do(pipeline.run)

        print(f"⏰ Hourly pipeline scheduled every {args.interval} minutes. Press Ctrl+C to stop.")
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nPipeline stopped by user.")
    else:
        # Monthly mode - run once
        pipeline.run()
        print("✅ Monthly pipeline completed.")


if __name__ == "__main__":
    main()