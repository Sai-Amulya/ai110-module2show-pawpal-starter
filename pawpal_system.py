from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import date
from uuid import uuid4

# -------------------------
# Core Data Objects
# -------------------------

@dataclass
class Task:
    id: str = field(default_factory=lambda: str(uuid4()))
    name: str
    duration: float
    priority: str
    pet: 'Pet'
    time_window: Optional[str] = None

    def update_task(self, name: Optional[str] = None, duration: Optional[float] = None,
                    priority: Optional[str] = None, time_window: Optional[str] = None):
        pass

    def is_schedulable(self, available_time: float) -> bool:
        pass

    def describe(self) -> str:
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    owner: 'Owner' 
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def remove_task(self, task_id: int):
        pass

    def list_tasks(self) -> List[Task]:
        pass

# -------------------------
# Higher-level Objects
# -------------------------

class Owner:
    def __init__(self, name: str, available_time: float, preferences: Optional[Dict] = None):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences or {}
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def update_preferences(self, preferences: Dict):
        pass

    def get_daily_availability(self) -> float:
        pass


class Schedule:
    def __init__(self, owner: Owner, schedule_date: date):
        self.owner = owner
        self.date = schedule_date
        self.tasks: List[Task] = []
        self.explanations: List[str] = []

    def generate(self, tasks: List[Task], owner: Owner):
        pass

    def add_task(self, task: Task):
        pass

    def remove_task(self, task: Task):
        pass

    def explain(self) -> List[str]:
        pass

    def display(self):
        pass
    
    def list_pets(self) -> List[Pet]:
        """Return a list of unique pets from the scheduled tasks."""
        return list({task.pet for task in self.tasks})

class Scheduler:
    def __init__(self, tasks: List[Task], constraints: Optional[Dict] = None):
        self.tasks = tasks
        self.constraints = constraints or {}

    def sort_tasks(self):
        pass

    def fit_tasks_into_day(self):
        pass

    def resolve_conflicts(self):
        pass

    def generate_daily_plan(self, owner: Owner, schedule_date: date) -> Schedule:
        pass

