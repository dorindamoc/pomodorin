from pydantic import BaseModel, Field


class AppSettings(BaseModel):
    pomodoro_minutes: int = Field(default=25, ge=1, le=120)
    short_break_minutes: int = Field(default=5, ge=1, le=60)
    long_break_minutes: int = Field(default=15, ge=1, le=60)
    long_break_interval: int = Field(default=4, ge=1, le=10)
    auto_start_next: bool = False
