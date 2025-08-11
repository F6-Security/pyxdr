__version__ = "1.0.1"

XDR_API_KEY = "XDR_API_KEY"
XDR_API_URL = "XDR_API_URL"
XDR_VERIFY_SSL = "XDR_VERIFY_SSL"
XDR_CONNECTION_RETRIES = "XDR_CONNECTION_RETRIES"
XDR_CONNECTION_TIMEOUT = "XDR_CONNECTION_TIMEOUT"
XDR_PROXIES = "XDR_PROXIES"
XDR_USER_AGENT = "XDR_USER_AGENT"

DEFAULTS = {
    XDR_API_URL: "https://xdr.f6.security/",
    XDR_VERIFY_SSL: True,
    XDR_CONNECTION_RETRIES: 3,
    XDR_CONNECTION_TIMEOUT: 10,
    XDR_PROXIES: {},
    XDR_USER_AGENT: "pyxdr v" + __version__
}


class Status:
    IN_PROGRESS = "IN PROGRESS"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


class Language:
    RU = "ru"
    EN = "en"


class Resolution:
    r800x600 = "800x600"
    r1024x768 = "1024x768"
    r1152x1024 = "1152x1024"
    r1280x1024 = "1280x1024"
    r1600x1200 = "1600x1200"


class OpSystem:
    WIN_XP = "winxp"
    WIN_7 = "win7"
    WIN_10 = "w10"


class Capacity:
    x86 = "x86"
    x64 = "x64"


class Url:
    API = "api/"

    ANALGIN_UPLOAD = API + "analgin/upload/"

    ATTACHES = API + "attaches/"
    ATTACH = ATTACHES + "?id={}"

    REPORT = ATTACHES + "{attach_id}/{commit}/{report_id}/mdp_report/"
    UI_REPORT = "warehouse/{commit}/{report_id}/attaches/{attach_id}/"

    EXPORT_REPORT = ATTACHES + "{attach_id}/{commit}/{report_id}/mdp_report_export/"
    EXPORT_PDF_REPORT = EXPORT_REPORT + '?report_export_format=pdf'
    EXPORT_PCAP = ATTACHES + '{attach_id}/{commit}/{report_id}/dump.pcap/dump.pcap/mdp_report_file_download/'
    EXPORT_VIDEO = ATTACHES + '{attach_id}/{commit}/{report_id}/shots/video.webm/video.webm/mdp_report_file_download/'
    
    HASH_REPUTATION = API + 'warehouse/check_hash/{}/{}/'


class Method:
    GET = 'GET'
    POST = 'POST'
