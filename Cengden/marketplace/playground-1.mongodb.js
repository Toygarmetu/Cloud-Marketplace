/* global db */
// MongoDB Playground

// Select the database to use.
use('cengden_db');

// Insert new private lesson documents into the private_lessons collection.
db.getCollection('private_lessons').insertMany([
  {
    Title: "Programming Fundamentals Course",
    Tutor_Name: "John Smith",
    Lessons: ["Data Structures", "Algorithms", "C++"],
    Location: "Online",
    Duration: "1 hour/session",
    Price: "$60",
    Image: "null", // Replace with the actual path to the image
    Description: "Comprehensive course covering programming fundamentals including Data Structures, Algorithms, and C++."
  },
  {
    Title: "Python Programming Course",
    Tutor_Name: "Emily Johnson",
    Lessons: ["Python Programming"],
    Location: "In-Person (Studio)",
    Duration: "45 minutes/session",
    Price: "$50",
    Image: "null", // Replace with the actual path to the image
    Description: "Learn Python programming from scratch or improve your existing skills with personalized lessons."
  }
]);

console.log('New private lessons have been inserted into the database.');
