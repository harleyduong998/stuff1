from flask import Flask, render_template

app = Flask(__name__)

# Mock data for friends
FRIENDS = [
    {"id": 1, "name": "Nguyễn Văn A", "avatar": "https://i.pravatar.cc/150?u=1"},
    {"id": 2, "name": "Trần Thị B", "avatar": "https://i.pravatar.cc/150?u=2"},
    {"id": 3, "name": "Lê Văn C", "avatar": "https://i.pravatar.cc/150?u=3"},
    {"id": 4, "name": "Phạm Minh D", "avatar": "https://i.pravatar.cc/150?u=4"},
    {"id": 5, "name": "Hoàng Anh E", "avatar": "https://i.pravatar.cc/150?u=5"},
    {"id": 6, "name": "Đỗ Hùng F", "avatar": "https://i.pravatar.cc/150?u=6"},
    {"id": 7, "name": "Bùi Tiến G", "avatar": "https://i.pravatar.cc/150?u=7"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_lixi():
    # In a real app, QR code would be generated here or fetched
    qr_code_url = "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=Lì_Xì_Tết_2024"
    return render_template('create_lixi.html', friends=FRIENDS, qr_code_url=qr_code_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
