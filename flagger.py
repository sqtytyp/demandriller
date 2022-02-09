# TODO: links refactoring : https://mailchimp.com/developer/transactional/docs/activity-reports/#click-tracking
# https://coderzcolumn.com/tutorials/python/email-how-to-represent-an-email-message-in-python
# TODO: sprawdzic najpierw jak to wyglada z calym mailem bez rozbijania na body i skladania znowu w calosc
# TODO: sprawdzi o co chodzi z tym HEADEREM MANDRILLA https://mailchimp.com/developer/transactional/docs/smtp-integration/#x-mc-track
# bo moze wystarczy dodac header X-MC-Track: disable
from email.message import EmailMessage


def flag_by_header(flagged_msg: EmailMessage):
    # TODO: zrobic add_content do headera

    return flagged_msg


def flag_by_param(flagged_msg: EmailMessage):
    # TODO: regexem dodac param
    return flagged_msg
