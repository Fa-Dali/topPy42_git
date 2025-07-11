-- Включаем расширение для UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Таблица Факультеты (Facultie)
CREATE TABLE Facultie (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Financing MONEY DEFAULT 0::money NOT NULL CHECK((Financing::numeric) >= 0),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name <> '')
);

-- Таблица Кафедра (Department)
CREATE TABLE Department (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Financing MONEY DEFAULT 0::money NOT NULL CHECK((Financing::numeric) >= 0),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name <> ''),
    FacultyId UUID REFERENCES Facultie(Id) ON DELETE CASCADE NOT NULL
);

-- Таблица Кураторы (Curator)
CREATE TABLE Curator (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name VARCHAR(225) NOT NULL CHECK(Name <> ''),
    Surname VARCHAR(225) NOT NULL CHECK(Surname <> '')
);

-- Таблица Группа (Groups)
CREATE TABLE Groups (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name VARCHAR(20) UNIQUE NOT NULL CHECK(Name <> ''),
    Year INT NOT NULL CHECK(Year BETWEEN 1 AND 5),
    DepartmentId UUID REFERENCES Department(Id) ON DELETE CASCADE NOT NULL
);

-- Таблица Группы и кураторы (GroupCurator)
CREATE TABLE GroupCurator (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    CuratorId UUID REFERENCES Curator(Id) ON DELETE CASCADE NOT NULL,
    GroupId UUID REFERENCES Groups(Id) ON DELETE CASCADE NOT NULL
);

-- Таблица Предметы (Subject)
CREATE TABLE Subject (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name VARCHAR(100) UNIQUE NOT NULL CHECK(Name <> '')
);

-- Таблица Преподаватели (Teacher)
CREATE TABLE Teacher (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    Name VARCHAR(225) NOT NULL CHECK(Name <> ''),
    Salary MONEY NOT NULL CHECK((Salary::numeric) > 0),
    Surname VARCHAR(225) NOT NULL CHECK(Surname <> '')
);

-- Таблица Лекции (Lecture)
CREATE TABLE Lecture (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    LectureRoom VARCHAR(225) NOT NULL CHECK(LectureRoom <> ''),
    SubjectId UUID REFERENCES Subject(Id) ON DELETE CASCADE NOT NULL,
    TeacherId UUID REFERENCES Teacher(Id) ON DELETE CASCADE NOT NULL
);

-- Таблица Группы и лекции (GroupLecture)
CREATE TABLE GroupLecture (
    Id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    GroupId UUID REFERENCES Groups(Id) ON DELETE CASCADE NOT NULL,
    LectureId UUID REFERENCES Lecture(Id) ON DELETE CASCADE NOT NULL
);