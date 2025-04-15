from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_products():
    return [{"id": 1, "name": "Café Arabica"}, {"id": 2, "name": "Café Robusta"}]
