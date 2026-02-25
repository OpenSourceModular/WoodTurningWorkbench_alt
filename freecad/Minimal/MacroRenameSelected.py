# -*- coding: utf-8 -*-
"""FreeCAD macro: rename selected objects by label with a base name + 001.

- Prompts for a base name.
- Applies labels like <base>001, <base>002, ... to current selection.
"""

import FreeCAD
import FreeCADGui

try:
    from PySide2 import QtWidgets
except Exception:  # pragma: no cover - fallback for older FreeCAD
    from PySide import QtGui as QtWidgets


def _prompt_base_name():
    return QtWidgets.QInputDialog.getText(
        None,
        "Rename Selected",
        "Base name (labels will be <base>001, <base>002, ...):",
    )


def _get_selection():
    try:
        return FreeCADGui.Selection.getSelection()
    except Exception:
        return []


def rename_selected_labels():
    selection = _get_selection()
    if not selection:
        FreeCAD.Console.PrintMessage("No objects selected.\n")
        return

    base_name, ok = _prompt_base_name()
    if not ok:
        return

    base_name = (base_name or "").strip()
    if not base_name:
        FreeCAD.Console.PrintMessage("No base name provided.\n")
        return

    for index, obj in enumerate(selection, start=1):
        obj.Label = f"{base_name}{index:03d}"

    try:
        FreeCAD.ActiveDocument.recompute()
    except Exception:
        pass


if __name__ == "__main__":
    rename_selected_labels()
