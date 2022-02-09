import importlib
import os
import sys

# has to be at root


"""
IMPORT ORDER

### USER INTERFACE

->  from _blender.interface import
        install_dependencies,
        ui_registration
    import m_CONST
importlib.reload(install_dependencies)
importlib.reload(log)
importlib.reload(stream_detection_operator)

### BPY RIGGING
importlib.reload(m_V)
importlib.reload(constraints)
importlib.reload(m_CONST)
importlib.reload(objects)
importlib.reload(abs_rigging)
importlib.reload(limb_drivers)
importlib.reload(log)

### BRIDGE
importlib.reload(objects)
importlib.reload(log)
importlib.reload(m_CONST)
importlib.reload(m_V)
importlib.reload(abs_assignment)

### DETECTION
importlib.reload(pose_drivers)
importlib.reload(abstract_detector)
importlib.reload(abstract_detector)
importlib.reload(pose_drivers)
importlib.reload(hand_drivers)
importlib.reload(abstract_detector)
importlib.reload(face_drivers)
importlib.reload(abstract_detector)


"""
