import os
import json
from os import listdir
from os.path import isfile, join

# This is the Project Root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Database:
    def get_note_by_id(self, userid, noteid):
        note_file = os.path.join(ROOT_DIR, 'v1/service/{0}/{1}'.format(userid, noteid))
        with open(note_file) as f:
            content = f.readlines()
        content = [x.strip() for x in content]     
        return json.dumps(content)

    def get_all_notes(self, userid):
        note_dir = os.path.join(ROOT_DIR, 'v1/service/{}'.format(userid))
        onlyfiles = [f for f in listdir(note_dir) if isfile(join(note_dir, f))]
        all_notes=list()
        for note in onlyfiles:
            with open(note) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            all_notes.append(content)
        return json.dumps(all_notes)