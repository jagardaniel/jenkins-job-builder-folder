import xml.etree.ElementTree as XML

import jenkins_jobs.modules.base


class Folder(jenkins_jobs.modules.base.Base):
    sequence = 0

    def root_xml(self, data):
        xml_parent = XML.Element('com.cloudbees.hudson.plugins.folder.Folder')

        return xml_parent
