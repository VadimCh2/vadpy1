import utils
from pywebio.input import input, input_group
from pywebio.output import put_success
from pywebio import start_server
from pywebio.session import run_js
import constants


def main():
    data = input_group(
        "String Length",
        [
            input("Name", name="name", required=True),
            input("String", name="text", required=True),
            input("Email", name="email", required=True),
        ]
    )

    text = data["text"].strip()

    string_info = {
        "name": data["name"],
        "text": text,
        "length": len(text),
    }

    email_body = utils.create_string_report(string_info)

    utils.send_email(
        [data["email"]],
        email_body,
        mail_subject=constants.MAIL_SUBJECT,
    )

    put_success("Email was sent successfully!")

    run_js("""
        setTimeout(() => {
            window.location.reload();
        }, 5000);
    """)


start_server(
    main,
    host="0.0.0.0",
    port=8888,
    debug=True,
)