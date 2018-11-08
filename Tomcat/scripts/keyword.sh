count=$(ps -ef | grep tomcat | wc -l | sed -e 's/ //g')

echo '<?xml version="1.0"?>'
echo '<items>'

if [ "$count" == "1" ]; then
  action="Start up"
  icon="startup.png"
  arg=$TOMCAT_PATH$"/bin/startup.sh"
else
  action="Shut down"
  icon="shutdown.png"
  arg=$TOMCAT_PATH$"/bin/shutdown.sh"
fi
  
cat <<_END_OF_ITEM_
  <item uid="" arg="$arg">
    <title>$action Tomcat</title>
	<subtitle>$arg</subtitle>
    <icon>$icon</icon>
  </item>
_END_OF_ITEM_

echo '</items>'