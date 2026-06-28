from fastapi import APIRouter

router = APIRouter(
    prefix="/notify",
    tags=["Notifications"]
)


@router.post("/send")
def send_notification():

    return {

        "status": "queued"

    }
