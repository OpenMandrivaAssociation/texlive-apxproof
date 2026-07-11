%global tl_name apxproof
%global tl_revision 79251

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.1
Release:	%{tl_revision}.1
Summary:	Proofs in appendix
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/apxproof
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apxproof.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes it easier to write articles where proofs and other
material are deferred to the appendix. The appendix material is written
in the LaTeX code along with the main text which it naturally
complements, and it is automatically deferred. The package can
automatically send proofs to the appendix, can repeat in the appendix
the theorem environments stated in the main text, can section the
appendix automatically based on the sectioning of the main text, and
supports a separate bibliography for the appendix material. It depends
on the following packages: amsthm, bibunits (if the bibliography option
is set to separate), environ, etoolbox, fancyvrb, ifthen, and kvoptions.

