import os


def get_files_by_grade_subject(grade, subjects):
    """
    This function gets a list of files for the given grade and subjects.

    Args:
        grade (str): The grade of the files to get.
        subjects (list[str]): The subjects of the files to get.

    Returns:
        A dictionary mapping from subject to a list of file names.
    """

    # Get the parent folder of the reference material.
    parent_folder = os.path.join(os.getcwd(), 'static', 'reference material')

    # Get the grade folder.
    grade_folder = os.path.join(parent_folder, grade)

    # Initialize a dictionary to store the files by subject.
    files_by_subject = {}

    # Iterate over the subjects.
    for subject in subjects:
        # Get the subject folder.
        subject_folder = os.path.join(grade_folder, subject)

        # Check if the subject folder exists.
        if os.path.exists(subject_folder):
            # Get a list of all the files in the subject folder.
            file_list = []
            for root, dirs, files in os.walk(subject_folder):
                for file in files:
                    file_name = os.path.basename(file)
                    file_list.append(file_name)

            # Add the list of files to the dictionary.
            files_by_subject[subject] = file_list
        else:
            # The subject folder does not exist, so add an empty list to the dictionary.
            files_by_subject[subject] = []

    # Return the dictionary of files by subject.
    return files_by_subject
