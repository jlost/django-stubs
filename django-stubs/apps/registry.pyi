import threading
from collections import OrderedDict
from typing import Any, Callable, List, Optional, Tuple, Type, Union, Iterable, DefaultDict, Dict

from django.db.migrations.state import AppConfigStub
from django.db.models.base import Model

from .config import AppConfig

class Apps:
    all_models: "Dict[str, OrderedDict[str, Type[Model]]]" = ...
    app_configs: "OrderedDict[str, AppConfig]" = ...
    stored_app_configs: List[Any] = ...
    apps_ready: bool = ...
    ready_event: threading.Event = ...
    loading: bool = ...
    _pending_operations: DefaultDict[Tuple[str, str], List]
    models_ready: bool = ...
    ready: bool = ...
    def __init__(self, installed_apps: Optional[Union[List[AppConfigStub], List[str], Tuple]] = ...) -> None: ...
    def populate(self, installed_apps: Union[List[AppConfigStub], List[str], Tuple] = ...) -> None: ...
    def check_apps_ready(self) -> None: ...
    def check_models_ready(self) -> None: ...
    def get_app_configs(self) -> Iterable[AppConfig]: ...
    def get_app_config(self, app_label: str) -> AppConfig: ...
    # it's not possible to support it in plugin properly now
    def get_models(self, include_auto_created: bool = ..., include_swapped: bool = ...) -> List[Type[Any]]: ...
    def get_model(self, app_label: str, model_name: Optional[str] = ..., require_ready: bool = ...) -> Type[Any]: ...
    def register_model(self, app_label: str, model: Type[Model]) -> None: ...
    def is_installed(self, app_name: str) -> bool: ...
    def get_containing_app_config(self, object_name: str) -> Optional[AppConfig]: ...
    def get_registered_model(self, app_label: str, model_name: str) -> Type[Model]: ...
    def get_swappable_settings_name(self, to_string: str) -> Optional[str]: ...
    def set_available_apps(self, available: List[str]) -> None: ...
    def unset_available_apps(self) -> None: ...
    def set_installed_apps(self, installed: Union[List[str], Tuple[str]]) -> None: ...
    def unset_installed_apps(self) -> None: ...
    def clear_cache(self) -> None: ...
    def lazy_model_operation(self, function: Callable, *model_keys: Any) -> None: ...
    def do_pending_operations(self, model: Type[Model]) -> None: ...

apps: Apps
