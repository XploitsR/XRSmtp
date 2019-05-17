# XRSmtp
XploitsR | XRSmtp is a module for fetching the details of any SMTP provider for your development or personal use.

# Usage
    # import the xrsmtp module
    import xrsmtp
    
    #XRSmtp returns an a list which can be accessed with only 0 and 1 index
    xr = xrsmtp.XRSmtp()
    
    # For SSL
    smtp_server = xr.smtp_portSSL("your-smtp-providers-name")[0] #example: Gmail
    smtp_port = xr.smtp_portSSL("your-smtp-providers-name")[1] #example: Gmail
    
    
    # For TLS
    smtp_server = xr.smtp_portTLS("your-smtp-providers-name")[0] #example: Gmail
    smtp_port = xr.smtp_portTLS("your-smtp-providers-name")[1] #example: Gmail
    
    
    # [0] is used to retrieve the smtp server from the returned list
    # [1] is used to retrieve the smtp server's port from the returned list
    
    
    # You can list all possible smtp provider names XRsmtp module has using
    smtp_listAll()
    
    example: 
        smtps = xr.smtp_listAll()
        print("SMTP provider names ", smtps)
