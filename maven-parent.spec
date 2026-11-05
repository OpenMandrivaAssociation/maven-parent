Name:           maven-parent
Version:        50
Release:        1
Summary:        Apache Maven parent POM
License:        ASL 2.0
URL:            https://maven.apache.org
Source0:        https://github.com/apache/maven-parent/archive/refs/tags/maven-parent-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
# The tag is a reactor. This package publishes the parent POM only.
BuildOption:	-N validate

%description
Apache Maven parent POM file used by other Maven projects.

%prep
%setup -q -n maven-parent-maven-parent-%{version}
# maven-plugins and maven-shared-components are their own packages.
# Leaving <modules> makes install publish those coordinates from this tree.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text = re.sub(r"\n  <modules>.*?</modules>", "", text, count=1, flags=re.S)
path.write_text(text)
PY

%files -f .mfiles
%doc LICENSE README.md
