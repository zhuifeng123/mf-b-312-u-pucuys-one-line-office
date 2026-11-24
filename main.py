import os

JOKE = (
    "Per my last email, the meeting could've been an email, "
    "which we could've skipped, which is why I sent a memo about it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
