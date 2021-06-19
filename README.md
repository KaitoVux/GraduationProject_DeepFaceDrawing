# Đồ án tốt nghiệp: Tái tạo khuôn mặt người từ nét phác thảo

## Trường Đại Học Khoa học tự nhiên

### Khoa công nghệ thông tin

## Nhóm sinh viên thực hiện:

Vũ Trọng Đạt - Nguyễn Hoàng Chiến - Nguyễn Phục Dược - Nguyễn Trường An - Nguyễn Ngọc Chung Chí

## Giới thiệu

Để tiện lợi hơn cho việc nghiên cứu hiệu suất của mô hình. Chúng tôi đã phát triển một ứng dụng cho phép người dùng tải ảnh phác thảo lên và thay đổi các nét vẽ trực tiếp trên đó, sau đó, ảnh phác thảo đó sẽ được tái tạo thành một ảnh khuôn mặt của người thật một cách trực tiếp theo thời gian thực.

Chúng tôi đã sử dụng các công nghệ sau để tạo nên ứng dụng này:

Thư viện PyQt5: được sử dụng để xây dựng giao diện người dùng

Thư viện Jittor: được sử dụng để xây dựng mô hình mạng học sâu, qua đó suy diễn và tái tạo ảnh mặt người từ ảnh đầu vào

## Yêu cầu

1. Phần cứng

-   Ubuntu 16.04 hoặc mới hơn

-   NVIDIA GPU + CUDA 9.2

2. Phần mềm

-   Python 3.7

-   Jittor. More details in <a href="https://github.com/Jittor/Jittor" target="_blank">Jittor</a>

```
sudo apt install python3.7-dev libomp-dev

sudo python3.7 -m pip install git+https://github.com/Jittor/jittor.git

python3.7 -m jittor.test.test_example
```

-   Cài đặt

```
sh install.sh
```

## Cách sử dụng

Chạy câu lệnh sau để sử dụng:

```
python3.7 demo.py
```
