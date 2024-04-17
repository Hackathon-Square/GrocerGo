INSERT INTO UserData (Role, UserName, Email, Password_hash)
values (
        'Admin',
        'Admin',
        'Admin@gmail.com',
        '$2y$10$XDxr6VP9xcmv3QtVcZRZa.8h8zglNQgVr1Z4x.Hz1TK/NBG9sswDi'
    )
/*
Admin掌握用户的提交内容的审查，账户手动创建，用户名为Admin，邮箱为Admin@gmail.com，密码为SquareAdmin。创建时传入php的hash算法得到的hash值。
*/