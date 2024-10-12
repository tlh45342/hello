#
# spec file for package hello
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           hello
Version:        1
Release:        0
Summary:        This is a summary
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#
spdx-licenses
License:        GPL-2.0-or-later
URL:            http://github/tlh45342/x.zip
Source:         hello-1.tar

%description

%prep
%setup -q

%build
