@echo off
call "bat\install_travis.bat"
call "bat\encrypt_pypi_password.bat"
call "generate_without_travis.bat"