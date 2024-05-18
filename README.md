# Quick Start
1. コンテナを起動する
```
docker compose up --build
```
2. サーバにアクセスする
```
http://localhost:5001
```

# POST PUT DELETEメソッドの実行
### POST
```
curl -X POST https://exmamle.com -d "name=my-folder"
```

### PUT
```
curl -X PUT https://exmamle.com -d "name=rename"
```

### DELETE
```
curl -X DELETE https://exmamle.com
```

# Gitの操作
### ブランチの新規作成 & ブランチの切り替え
```
$ git switch -c <ブランチ名>
```

### ブランチの切り替え
```
$ git switch <ブランチ名>
```

### ブランチ名の変更
```
$ git branch -m <古いブランチ名> <新しいブランチ名>
```
- 今開いているブランチの名前を変更したい場合
```
$ git branch -m <新しいブランチ名>
```

### git addしていないファイルを元に戻す
```
$ git checkout <ファイル名>
```

### git addしたファイルを元に戻す
```
$ git reset <ファイル名>
```

# DBテーブル設計
## Foldersテーブル
- id : integer, primary key, autoincrement
- name : string
- created_at : string
- updated_at : string
- places_id : foreign key, integer

## Placesテーブル
- id : integer, primary key, autoincrement
- name : string
- address : string
- image_url : string
- memo : string
- created_at : string
- updated_at : string
- user_id : foreign key, integer

## Usersテーブル
- id : integer, primary key, autoincrement
- name : string
- email : string
- password : string
- created_at : string
- updated_at : string

## 変更
FolderモデルとPlaceモデルは1対多の関係なので以下のように定義を変更します.
### Foldersテーブル
```diff
1. id : integer, primary key, autoincrement
2. name : string
3. created_at : string
4. updated_at : string
- places_id : foreign key, integer
```

### Placesテーブル
```diff
1. id : integer, primary key, autoincrement
2. name : string
3. address : string
4. image_url : string
5. memo : string
6. created_at : string
7. updated_at : string
8. user_id : foreign key, integer
+ folder_id : foreign key, integer
```


# エンドポイント
### folders/
- GET
```
{
    {
        id : 1,
        name : "Hoge",
        created_at : 2024-05-15,
        updated_at : 2024-05-20,
        place_id: 1
    },
    {
        id : 2,
        name : "Fuga",
        created_at : 2024-05-14,
        updated_at : 2024-05-28,
        place_id: 3
    }
}
```

- POST


新しいフォルダを作成する.
フォルダ名と作成日を追加する.
```
{
    status : 200,
    message : "Successfully created a new folder!"
}
```


### folers/int:folder_id
http://localhost/folders/1 を例にする.

- GET
```
{
    id : 1,
    name : "Hoge",
    created_at : 2024-05-15,
    updated_at : 2024-05-20,
    place_id: 1
}
```

- PUT


folder_idが1のフォルダの名前を変更する.
updated_atに日付を追加する.
```
{
    status : 200,
    message : "Successfully renamed the folder!"
}
```

- DELETE


folder_idが1のフォルダを削除する.
```
{
    status : 200,
    message : "Successfully deleted the folder!"
}
```


### places/

- GET
```
{
    {
        id : 1,
        name : "神戸",
        address : "670-0012 兵庫県神戸市",
        image_url : "https://exmaple.com",
        memo : "楽しかった！",
        created_at : 2024-05-17,
        updated_at : 2-24-09-12,
        user_id : 1
    },
    {
        id : 2,
        name : "北海道",
        address : "",
        image_url : "https://exmaple.com/contents",
        memo : "楽しかった！",
        created_at : 2024-05-27,
        updated_at : 2-24-09-02,
        user_id : 2
    }
}
```

- POST


新しい場所を作成する.
場所名と作成日を追加する.
```
{
    status : 200,
    message : "Successfully created a new location!"
}
```


### places/int:place_id

http://localhost/places/1を例にする.

- GET
```
{
    id : 1,
    name : "神戸",
    address : "670-0012 兵庫県神戸市",
    image_url : "https://exmaple.com",
    memo : "楽しかった！",
    created_at : 2024-05-17,
    updated_at : 2-24-09-12,
    user_id : 1
}
```

- PUT


place_idが1の場所の名前を変更する. or メモを変更する or 住所を変更する or 画像を変更する.
updated_atに日付を追加する.

場所の名前を変更したら
```
{
    status : 200,
    message : "Successfully renamed the location!"
}
```
メモを変更したら
```
{
    status : 200,
    message : "Successfully renamed the memo!"
}
```
住所を変更したら
```
{
    status : 200,
    message : "Successfully renamed the address!"
}
```
画像を変更したら
```
{
    status : 200,
    message : "Successfully renamed the image url!"
}
```

- DELETE


place_idが1の場所を削除する.
```
{
    status : 200,
    message : "Successfully deleted the location!"
}
```


### signin/
- POST


ユーザの名前, メールアドレス, パスワードがフロントエンドから送られる.
```
{
    status : 200,
    message: "Successfully created the user!"
}
```


### login/int:user_id
http://localhsot/login/1 を例にする.
- GET
```
{
    id : 1,
    name : "root",
    email : "exmaple@gmail.com",
    password : "p@ssw0rd",
    created_at : 2024-05-01,
    updated_at : null
}
```

- PUT


ユーザ名を変更 or メールアドレスを変更 or パスワードを変更.
変更日時を保存する.

ユーザ名を変更した場合
```
{
    status : 200,
    message: "Successfully renamed the name!"
}
```
メールアドレスを変更した場合
```
{
    status : 200,
    message: "Successfully renamed the email!"
}
```
パスワードを変更した場合
```
{
    status : 200,
    message: "Successfully renamed the password!"
}
```

### delete/int:user_id
http://localhsot/delete/1 を例にする.
- DELETE


user_idが1のユーザを削除.
```
{
    status : 200,
    message: "Successfully deleted the user!"
}
```
