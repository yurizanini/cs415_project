INSERT INTO PhoneType (phone_type_id)
    VALUES(
        1
    );
INSERT INTO UserPhone (user_phone_id, phone_type_id, phone_number, created_date)
    VALUES(
        2,
        1,
        '3851231234',
        now()
    );