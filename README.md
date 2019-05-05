# 7750-ConfGen
A faster, easier way to build a virtual lab configuration for the Nokia 7750s utilizing Netmiko, Jinja2 and Yaml. 

This project is aimed at speeding up the configuration process of a virtual lab. 
The project utilizes Netmiko to configure devices. Therefore, IP connectivity must be established before utilizing the scripts.

Things to note regarding the configuration:

The template takes advantage of a policy-statement to create a full-mesh of MPLS LSPs.
  - Utilizes OSPF with Traffic-Engineering. However, the MPLS-LSPs are hard set to Facility Fast Re-Route only.
The template includes a pw-template and leverages BGP-AD(Auto-Discovery) to auto-create MESH-SDPs across a VPLS.
The template includes an LDP template to establish Targeted-LDP sessions.


