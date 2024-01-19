CREATE TABLE User (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(25),
    last_name VARCHAR(30),
    email VARCHAR(40),
    pass_word VARCHAR(40),
    created_date DATETIME,
    user_name VARCHAR(40),
    PRIMARY KEY (user_id)
);

CREATE TABLE UserAddress (
    user_address_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    address_1 VARCHAR(30),
    address_2 VARCHAR(30),
    city VARCHAR(25),
    st VARCHAR(2),
    zip VARCHAR(10),
    country VARCHAR(30),
    PRIMARY KEY (user_address_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE PhoneType (
    phone_type_id INT NOT NULL,
    PRIMARY KEY (phone_type_id)
);

CREATE TABLE UserPhone (
    user_phone_id INT NOT NULL,
    phone_type_id INT NOT NULL,
    phone_number VARCHAR(20),
    created_date DATETIME,
    user_id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (user_phone_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (phone_type_id) REFERENCES PhoneType(phone_type_id)
);

CREATE TABLE Services(
    service_id INT NOT NULL AUTO_INCREMENT,
    service_description VARCHAR(100),
    price INT NOT NULL,
    PRIMARY KEY (service_id)
);

CREATE TABLE `Order` (
    order_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date DATETIME,
    total_amount DECIMAL(10, 2),
    status VARCHAR(20),
    PRIMARY KEY (order_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE OrderServices(
    order_service_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    service_id INT NOT NULL,
    PRIMARY KEY (order_service_id),
    FOREIGN KEY (order_id) REFERENCES `Order`(order_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);