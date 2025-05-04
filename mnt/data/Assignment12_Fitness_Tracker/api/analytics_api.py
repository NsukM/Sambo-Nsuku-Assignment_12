from fastapi import APIRouter
from services.analytics_report_service import AnalyticsReportService

router = APIRouter()
service = AnalyticsReportService()

@router.get("/reports/summary")
def generate_summary():
    return service.generate_summary()


