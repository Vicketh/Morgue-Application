CREATE DATABASE morgue;

CREATE TABLE bodies (
  body_id INT PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  primary_contact TEXT NOT NULL,
  cause_of_death TEXT NOT NULL,
  date_of_arrival TEXT NOT NULL
);
CREATE TABLE invoices (
  invoice_id INT PRIMARY KEY,
  body_id INT NOT NULL,
  date_issued TEXT NOT NULL,
  amount_due REAL NOT NULL,
  paid BOOLEAN NOT NULL,
  FOREIGN KEY (body_id) REFERENCES bodies (body_id)
);
CREATE TABLE users (
    username STRING NOT NULL,
    password STRING 
);