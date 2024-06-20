from enum import Enum, IntFlag

class Locale(Enum):
    ID = "id"
    DA = "da"
    DE = "de"
    EN_GB = "en-GB"
    EN_US = "en-US"
    ES_ES = "es-ES"
    ES_419 = "es-419"
    FR = "fr"
    HR = "hr"
    IT = "it"
    LT = "lt"
    HU = "hu"
    NL = "nl"
    NO = "no"
    PL = "pl"
    PT_BR = "pt-BR"
    RO = "ro"
    FI = "fi"
    SV_SE = "sv-SE"
    VI = "vi"
    TR = "tr"
    CS = "cs"
    EL = "el"
    BG = "bg"
    RU = "ru"
    UK = "uk"
    HI = "hi"
    TH = "th"
    ZH_CN = "zh-CN"
    JA = "ja"
    ZH_TW = "zh-TW"
    KO = "ko"

class InteractionResponseType(Enum):
    PONG = 1
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9
    PREMIUM_REQUIRED = 10 # Deprecated

class MessageFlags(IntFlag):
    CROSSPOSTED = 1 << 0  # this message has been published to subscribed channels (via Channel Following)
    IS_CROSSPOST = 1 << 1  # this message originated from a message in another channel (via Channel Following)
    SUPPRESS_EMBEDS = 1 << 2  # do not include any embeds when serializing this message
    SOURCE_MESSAGE_DELETED = 1 << 3  # the source message for this crosspost has been deleted (via Channel Following)
    URGENT = 1 << 4  # this message came from the urgent message system
    HAS_THREAD = 1 << 5  # this message has an associated thread, with the same id as the message
    EPHEMERAL = 1 << 6  # this message is only visible to the user who invoked the Interaction
    LOADING = 1 << 7  # this message is an Interaction Response and the bot is "thinking"
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8  # this message failed to mention some roles and add their members to the thread
    SUPPRESS_NOTIFICATIONS = 1 << 12  # this message will not trigger push and desktop notifications
    IS_VOICE_MESSAGE = 1 << 13  # this message is a voice message
