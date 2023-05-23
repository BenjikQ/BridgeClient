from pathlib import Path
from timeit import default_timer as timer

from invoke import Context, task

ui_file_extension = ".ui"
converted_file_prefix = "ui_"
ui_path = Path("bridge/ui")

ui_files = [
    ui_file
    for ui_file in ui_path.iterdir()
    if ui_file.is_file() and ui_file.suffix == ui_file_extension
]
converted_files = [
    file
    for file in ui_path.iterdir()
    if file.is_file() and file.name[:3] == converted_file_prefix
]


@task()
def convert_ui(context: Context) -> float:
    execution_time = 0.0
    print("Converting .ui files")
    for ui_file in ui_files:
        print(f"  • Compiling {ui_file}")
        start = timer()
        context.run(f"pyuic6 {ui_file} -o {ui_file.parent}/ui_{ui_file.stem}.py")
        end = timer()
        execution_time += end - start

    if len(ui_files) == 1:
        print("1 file has been recompiled")
    else:
        print(f"{len(ui_files)} have been recompiled")
    return execution_time


@task()
def clean(_: Context) -> float:
    execution_time = 0.0
    print("Cleaning files")
    for file in converted_files:
        print(f"  • Removing {file}")
        start = timer()
        file.unlink()
        end = timer()
        execution_time += end - start
    return execution_time


@task()
def build(context: Context) -> None:
    execution_time = 0.0
    print("Building")
    for command in (clean, convert_ui):
        execution_time += command(context)  # type: ignore[operator]
    print(f"Finished in {execution_time}s")
