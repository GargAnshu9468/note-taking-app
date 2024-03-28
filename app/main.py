from crud import create_note, get_notes, get_note_by_id, update_note, delete_note
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from auth import router as auth_router
from auth import SECRET_KEY, ALGORITHM
from db_config import db
from models import Note
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal server error"})


@app.post("/notes", response_model=str)
async def create_new_note(note: Note, token: str = Depends(oauth2_scheme)):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.get_collection("users").find_one({"username": username})

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    note_id = create_note(note, username)

    return note_id


@app.get("/notes", response_model=list)
async def get_user_notes(token: str = Depends(oauth2_scheme)):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.get_collection("users").find_one({"username": username})

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    notes = get_notes(username)

    if not notes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notes not found")

    return notes


@app.get("/notes/{note_id}", response_model=Note)
async def get_notes_by_id(note_id: str, token: str = Depends(oauth2_scheme)):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.get_collection("users").find_one({"username": username})

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    note = get_note_by_id(note_id, username)

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    return note


@app.put("/notes/{note_id}", response_model=bool)
async def update_existing_note(note_id: str, note: Note, token: str = Depends(oauth2_scheme)):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.get_collection("users").find_one({"username": username})

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    success = update_note(note_id, note, username)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    return True


@app.delete("/notes/{note_id}", response_model=bool)
async def delete_existing_note(note_id: str, token: str = Depends(oauth2_scheme)):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.get_collection("users").find_one({"username": username})

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    success = delete_note(note_id, username)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")

    return True


app.include_router(auth_router)
