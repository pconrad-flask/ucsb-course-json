import json

import pprint   # pprint is "pretty print"


def printCourseDetails(course):
    print("%-12s %-20s %4d %-15s" %
          (course["course_id"],
          course["course_title"],
          course["capacity"],
          course["instructor"]) )

if __name__=="__main__":

  with open('courseData.json') as course_data:
    d = json.load(course_data)

  oneCourse = d['quarters'][0]['departments'][0]['courses'][0]
  #printCourseDetails(oneCourse)

  manyCourses = d['quarters'][0]['departments'][0]['courses']

  for c in manyCourses:
      printCourseDetails(c)

