import pikepdf

old_pdf = pikepdf.Pdf.open("sample_pdf.pdf")

no_extr = pikepdf.Permissions(extract=False)

old_pdf.save("encrypted_pdf.pdf",
             encryption=pikepdf.Encryption(
                 user="123abc",
                 owner="deep",
                 allow=no_extr))
