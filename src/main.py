from datetime import datetime, timezone


def main() -> None:
    print("zero-trust-policy-recommendation-agent initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
