import urllib.request
import tempfile
import tarfile
import shutil

class DependencyInstaller:
    """
    cherrypy releases: https://bitbucket.org/cherrypy/cherrypy/downloads
    """
    cherrypyurl = "https://bitbucket.org/cherrypy/cherrypy/get/default.tar.gz"
    cherrypysubfolder = os.path.join('cherrypy-cherrypy-efb777a00739','cherrypy')
    def __init__(self):
        cherrypytempfile = os.path.join(tempfile.gettempdir(),'cherrypy.tar.gz')
        cherrypytempdir =  os.path.join(tempfile.gettempdir(),'cherrypy')
        log.i('Downloading cherrypy...')
        with open(cherrypytempfile, 'wb') as f:
            urlhandler = urllib.request.urlopen(urllib.request.Request(DependencyInstaller.cherrypyurl))
            f.write(urlhandler.read())
        log.i('Extracting %s ' % cherrypytempfile)
        tarc = tarfile.open(cherrypytempfile,'r:gz')
        if os.path.exists(cherrypytempdir):
            log.w("Directory %s already exists." % cherrypytempdir)
            if 'y' == input('Do you want to delete its contents and proceed? [y/n]'):
                shutil.rmtree(cherrypytempdir)
            else:
                log.e("Cannot install cherrypy.")
                exit(1)
        os.mkdir(cherrypytempdir)
        tarc.extractall(cherrypytempdir)
        tarc.close()
        cherrymusicfolder = os.path.dirname(os.path.dirname(__file__))
        log.i('Copying cherrypy module inside cherrymusic folder (%s)...' % cherrymusicfolder)
        moduledir = os.path.join(cherrypytempdir,DependencyInstaller.cherrypysubfolder)
        shutil.copytree(moduledir,os.path.join(cherrymusicfolder,'cherrypy'))
        log.i('Cleaning up temporary files...')
        shutil.rmtree(cherrypytempdir)
        os.remove(cherrypytempfile)
        log.i('Successfully installed cherrymusic dependencies! You can now start cherrymusic.')
        
        
        