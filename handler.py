# TODO: catch incoming mail
import asyncio
from email import message_from_bytes
from email.policy import default
import checker
import flagger
import sender


class MailHandler:
    async def handle_DATA(self, server, session, envelope):
        peer = session.peer
        mailfrom = envelope.mail_from
        rcpttos = envelope.rcpt_tos
        rcptoptions = envelope.rcpt_options
        options = envelope.mail_options
        content = envelope.content
        originalcontent = envelope.original_content
        message = message_from_bytes(envelope.content, policy=default)
        body = message.get_body('html')

        messagetostring = message.as_string()  ### smtplib.sendmail WANTED BYTES or STRING, NOT email OBJECT.
        ### HERE HAPPENS TEXT PROCESSING, STRING SUBSTITUTIONS...
        ### THIS WAS MY CORE NEED, ASYNCWAIT ON EACH THREAD

        # print(type(envelope))  # <class 'aiosmtpd.smtp.Envelope'>
        # print(envelope)  # <aiosmtpd.smtp.Envelope object at 0x7fe4a159b910>
        # print(type(message))  # <class 'email.message.EmailMessage'>
        # print(message)  # message.get_content() == message
        # print(type(body))  # <class 'email.message.EmailMessage'>
        # print(body)  # zwraca tylko elementy html bez headera
        print(body)
        # print(messagetostring)
        await asyncio.sleep(1)
        checked_message = await checker.check()
        flagged_message = await flagger.flag_by_header(checked_message)
        sender.send(flagged_message)
        # server = smtplib.SMTP('localhost', 10027)
        # server.send_message(mailfrom, rcpttos, messagetostring)  ### NEEDED TO INVERT ARGS ORDER
        # server.quit()
        return '250 OK'
