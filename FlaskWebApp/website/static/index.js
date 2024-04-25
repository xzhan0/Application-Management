function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/home";
    });
}

function deleteCollege(collegeId) {
    fetch('/delete-college', {
        method: 'POST',
        body: JSON.stringify({ collegeId: collegeId})
    }).then((_res) => {
        window.location.href = "/application";
    });
}
