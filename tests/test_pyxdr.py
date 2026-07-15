from io import BytesIO
from unittest import TestCase
from pyxdr import MDP
from tests.utils import MockedClient, FAKE_API_TOKEN, MALICIOUS_URL, \
    ANALYSIS_ID, SHORT_INFO, REPORT, EXPORTED_REPORT, EXPORTED_PCAP, \
    EXPORTED_VIDEO, HASH_TYPE, HASH, HASH_REPUTATION


class TestMDP(TestCase):
    def setUp(self):
        self.mdp = MDP(FAKE_API_TOKEN)
        self.mdp.client = MockedClient()
    
    def test_upload_file(self):
        f = BytesIO(MALICIOUS_URL.encode())
        a = self.mdp.upload_file(f)
        self.assertEqual(a.id, ANALYSIS_ID)

    def test_upload_file_with_dll_analysis_options(self):
        f = BytesIO(MALICIOUS_URL.encode())
        self.mdp.upload_file(f, analyze_dll=True, analyze_all_dll=False)
        data = self.mdp.client.last_request["data"]
        self.assertIs(data["analyze_dll"], True)
        self.assertIs(data["analyze_all_dll"], False)
    
    def test_upload_url(self):
        analysis = self.mdp.upload_url(MALICIOUS_URL)
        self.assertEqual(analysis.id, ANALYSIS_ID)

    def test_upload_url_with_dll_analysis_options(self):
        self.mdp.upload_url(MALICIOUS_URL, analyze_dll=False, analyze_all_dll=True)
        data = self.mdp.client.last_request["data"]
        self.assertIs(data["analyze_dll"], False)
        self.assertIs(data["analyze_all_dll"], True)
    
    def test_get_info(self):
        analysis = self.mdp.upload_url(MALICIOUS_URL)
        info = analysis.get_info(extended=False)
        self.assertDictEqual(SHORT_INFO, info)
    
    def test_get_report(self):
        analysis = self.mdp.upload_url(MALICIOUS_URL)
        analysis.get_info(extended=False)
        report = analysis.get_report()
        self.assertDictEqual(report, REPORT)
    
    def test_export_report(self):
        analysis = self.mdp.upload_url(MALICIOUS_URL)
        analysis.get_info(extended=False)
        report = analysis.export_report()
        self.assertEqual(report, EXPORTED_REPORT)
    
    def test_export_pcap(self):
        analysis = self.mdp.upload_url(MALICIOUS_URL)
        analysis.get_info(extended=False)
        pcap = analysis.export_pcap()
        self.assertEqual(pcap, EXPORTED_PCAP)
    
    def test_export_video(self):
        analysis = self.mdp.upload_url(MALICIOUS_URL)
        analysis.get_info(extended=False)
        video = analysis.export_video()
        self.assertEqual(video, EXPORTED_VIDEO)

    def test_get_hash_reputation(self):
        r = self.mdp.get_hash_reputation(HASH_TYPE, HASH)
        self.assertDictEqual(r, HASH_REPUTATION)
