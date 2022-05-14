CREATE TABLE If NOT EXISTS tests (
    id SERIAL PRIMARY KEY,
    user_id int,
    score int,
    created_date DATE,

    CONSTRAINT fk_userId
        FOREIGN KEY(user_id)
            REFERENCES user_info(id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);

-- INSERT INTO tests (user_id, score, created_date) VALUES (1, 100, '2022-05-08');

CREATE TABLE IF NOT EXISTS image_spiral (
    id SERIAL PRIMARY KEY,
    test_id int,
    binary_data bytea,

    CONSTRAINT fk_testIdToSpiral
        FOREIGN KEY(test_id)
            REFERENCES tests(id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS image_wave (
    id SERIAL PRIMARY KEY,
    test_id int,
    binary_data bytea,

    CONSTRAINT fk_testIdToWave
        FOREIGN KEY(test_id)
            REFERENCES tests(id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);

