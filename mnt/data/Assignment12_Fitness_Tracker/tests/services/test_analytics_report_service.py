from services.analytics_report_service import AnalyticsReportService

def test_generate_summary():
    service = AnalyticsReportService()
    summary = service.generate_summary()
    assert "total_users" in summary


