CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Факультеты (Faculty)
CREATE TABLE Faculty (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name <> '')
);

-- Кафедры (Department)
CREATE TABLE Department (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Building INT NOT NULL CHECK(Building BETWEEN 1 AND 5),
    Financing MONEY NOT NULL DEFAULT '0'::MONEY CHECK(Financing >= '0'::MONEY),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name <> ''),
    FacultyId UUID NOT NULL REFERENCES Faculty(Id)
);

-- Кураторы (Curator)
CREATE TABLE Curator (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name TEXT NOT NULL CHECK(Name <> ''),
    Surname TEXT NOT NULL CHECK(Surname <> '')
);

-- Студенты (Student)
CREATE TABLE Student (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name TEXT NOT NULL CHECK(Name <> ''),
    Rating INT NOT NULL CHECK(Rating BETWEEN 0 AND 5),
    Surname TEXT NOT NULL CHECK(Surname <> '')
);

-- Преподаватели (Teacher)
CREATE TABLE Teacher (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    IsProfessor BOOLEAN NOT NULL DEFAULT FALSE,
    Name TEXT NOT NULL CHECK(Name <> ''),
    Salary MONEY NOT NULL CHECK(Salary > '0'::MONEY),
    Surname TEXT NOT NULL CHECK(Surname <> '')
);

-- Дисциплины (Subject)
CREATE TABLE Subject (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name <> '')
);

-- Группы (Groups)
CREATE TABLE Groups (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name VARCHAR(20) UNIQUE NOT NULL CHECK(Name <> ''),
    Year INT NOT NULL CHECK(Year BETWEEN 1 AND 5),
    DepartmentId UUID NOT NULL REFERENCES Department(Id)
);

-- Группы и кураторы (GroupCurator)
CREATE TABLE GroupCurator (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    CuratorId UUID NOT NULL REFERENCES Curator(Id),
    GroupId UUID NOT NULL REFERENCES Groups(Id)
);

-- Группы и студенты (GroupStudent)
CREATE TABLE GroupStudent (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    GroupId UUID NOT NULL REFERENCES Groups(Id),
    StudentId UUID NOT NULL REFERENCES Student(Id)
);

-- Лекции (Lecture)
CREATE TABLE Lecture (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Date DATE NOT NULL CHECK(Date <= CURRENT_DATE),
    SubjectId UUID NOT NULL REFERENCES Subject(Id),
    TeacherId UUID NOT NULL REFERENCES Teacher(Id)
);

-- Группы и лекции (GroupLecture)
CREATE TABLE GroupLecture (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    GroupId UUID NOT NULL REFERENCES Groups(Id),
    LectureId UUID NOT NULL REFERENCES Lecture(Id)
);