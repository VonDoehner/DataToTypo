from ftplib import FTP
from ftplib import FTP_TLS


x = "www.feg-hochdorf.ch"
y = "fegch_4"
z = "N1Us3kU97x"
u = '/Users/silvanzechner/Desktop/Predigtuploader/LOGO_Petrol_weiss.mp4'




class DataToTypo:

    def FTP(server_address, ftp_user, ftp_pw, ftpDirectory="Predigten"):
        
        # Create an FTP_TLS connection
        ftp = FTP_TLS(server_address)
        ftp.login(user=ftp_user, passwd=ftp_pw)

        # Enable SSL/TLS for the data channel
        ftp.prot_p()

        # List files in the remote directory
        hageri = ftp.retrlines('NLST')
        print(hageri)

        # Change to the remote directory where you want to upload the file
        remote_directory = 'Predigten'
        ftp.cwd(remote_directory)

        # Upload a file in binary mode
        with open(u, 'rb') as local_file:
            ftp.storbinary('STOR r_file.txtemote', local_file)

        ftp.quit()



DataToTypo.FTP(x, y, z)
