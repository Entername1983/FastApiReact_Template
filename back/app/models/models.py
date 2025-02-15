## We use this file for re-exporting all sql models in app, otherwise creates issues

from app.config.db import Base

print("Base", Base.metadata)  # noqa: T201
