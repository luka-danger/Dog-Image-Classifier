#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nate Edge
# DATE CREATED:                                 
# REVISED DATE: 6/24/24
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    # Creates list of files in directory
    pet_files = listdir(image_dir)
 
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
   
    # Iterates through every filename in the directory 
    for file in range(0, len(pet_files), 1):
       
      # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
      # isn't an pet image file
      if pet_files[file][0] != ".":
        
        
        # Creates temporary label variable to hold pet label name extracted 
        pet_label = ""

        # Format all labels to lower case and split at underscore("_")
        labels = pet_files[file].lower().split('_')

        # Iterate through characters (letters) in filename
        for char in labels: 
          # Only add if character is letter (alphabetical)
          if char.isalpha():
            # Add characters to pet_label
            # Join previously split file names with a space
            # Ex: Boston_Terrier --> 'boston terrier'
            pet_label = " ".join([pet_label, char])
        
        # Remove leading and trailing whitespace 
        pet_label = pet_label.strip()

        # Add filename to label if not in results_dictionary s
        if pet_files[file] not in results_dic:
          results_dic[pet_files[file]] = [pet_label]

        # Print error message to indicate a duplicate file added
        else:
            print("** Warning: Duplicate files exist in directory:", 
                  pet_files[file])
 
    return results_dic
