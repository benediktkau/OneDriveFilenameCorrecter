import logging
import os


class InvalidFilenameCorrecter:

    def __init__(self, path):
        self.path = path
        self.invalid_dir_count = 0
        self.invalid_file_count = 0
        self.files_in_invalid_dir = 0
        self.invalid_char_set = ('"', '*', ':', '<', '>', '&', '?', '|')

    def invalid_characters(self, filename):
        """ This method returns True if invalid characters were detected """

        for c in self.invalid_char_set:
            if c in filename:
                return True

        return False

    def correct_directories(self):
        """ This method ... """
        # Return all directories and files with os.walk
        full_directory = os.walk(self.path)

        # Iterate over all directories
        for directories in full_directory:
            filepath = directories[0]

            if self.invalid_characters(filepath):
                updated_filepath = self.replace_invalid_characters(filepath)

                # Print updated filepaths
                print('Invalid directory: ', filepath)
                print('Updated directory', updated_filepath)

                # increment counters
                self.invalid_dir_count += 1
                self.files_in_invalid_dir += len(directories[2])

                try:
                    os.rename(filepath, updated_filepath)
                except Exception:
                    logging.warning('Directory could not be renamed')

    def correct_filenames(self):
        full_directory = os.walk(self.path)

        # Iterate over all directories
        for directories in full_directory:

            # Iterate over all files in currently selected directory
            for filename in directories[2]:

                if self.invalid_characters(filename):

                    # increment counters
                    self.invalid_file_count += 1

                    full_filepath = directories[0] + '/' + filename

                    updated_filename = self.replace_invalid_characters(filename)
                    updated_full_filepath = directories[0] + '/' + updated_filename

                    # Print updated filepaths
                    print('Invalid filename: ', filename)
                    print('Updated filename:', updated_filename)
                    print('Full new filepath:', full_filepath)

                    try:
                        os.rename(full_filepath, updated_full_filepath)
                    except Exception:
                        logging.warning('File could not be renamed')



    def get_result(self):
        print(self.invalid_dir_count, 'invalid directory names have been found.')
        print(self.invalid_file_count, 'invalid filenames have been found.')
        print(self.files_in_invalid_dir, 'files in invalid directories that might not be synced.')
        print('Total: ', self.invalid_file_count + self.invalid_dir_count + self.files_in_invalid_dir)

    def replace_invalid_characters(self, string):
        for c in self.invalid_char_set:
            if c in string:
                string = string.replace(c, '_')
        return string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = InvalidFilenameCorrecter('/Users/benediktkau/OneDrive - University College London')
    test.correct_directories()
    test.correct_filenames()
    test.get_result()
