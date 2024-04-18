from random import randint


def mediweitnuto(message: str) -> str:
    message_lowercase = message.lower()
    message_builder = []
    for i in range(len(message)):
        if message_lowercase[i] in "о":
            message_builder.append(
                "а" if not message[i].isupper() else "А"
            )
            continue
        if message_lowercase[i] not in 'ндкрл':
            message_builder.append(message[i])
            continue

        if i > 1 and message_builder[i - 1].lower() == 'г':
            if randint(0, 100) > 10:
                message_builder.append(message[i])
                continue

            if i == len(message) - 1:
                continue

            if message[i + 1] != ' ':
                message_builder.append('')
                continue

        need_percent = (
            80 if message_lowercase[i] in 'рл' else 50
        )

        if randint(0, 100) > need_percent:
            message_builder.append(message[i])
            continue

        message_builder.append(
            "г" if not message[i].isupper() else "Г"
        )

    return "".join(message_builder)


if __name__ == "__main__":
    message = input()
    for i in range(10):
        print(mediweitnuto(message))
