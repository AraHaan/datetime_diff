@echo off
call "bat\install_travis.bat"
call "bat\encrypt_pypi_password.bat"
call "bat\test.bat"
call "bat\make_dists"
call "bat\upload.bat"
pause