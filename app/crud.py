from typing import List, Optional
from bson import ObjectId
from database import db
from models import Note


def create_note(note: Note, username: str):

    note_dict = note.dict()
    note_dict["user"] = username

    result = db.get_collection("notes").insert_one(note_dict)
    return str(result.inserted_id)


def get_notes(username: str) -> List[Note]:

    notes = db.get_collection("notes").find({"user": username})
    return [Note(**note) for note in notes]


def get_note_by_id(note_id: str, username: str) -> Optional[Note]:

    note = db.get_collection("notes").find_one({"_id": ObjectId(note_id), "user": username})
    return Note(**note) if note else None


def update_note(note_id: str, note: Note, username: str) -> bool:

    result = db.get_collection("notes").update_one(
        {
            "_id": ObjectId(note_id),
            "user": username
        },
        {
            "$set": note.dict(exclude_unset=True)
        }
    )

    return result.modified_count > 0


def delete_note(note_id: str, username: str) -> bool:

    result = db.get_collection("notes").delete_one({"_id": ObjectId(note_id), "user": username})
    return result.deleted_count > 0
