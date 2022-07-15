tar zxvf hadoop-3.3.2.tar.gz

nano ~/.bashrc

    export HADOOP_HOME=/home/hadoop/hadoop-3.3.2
    export HADOOP_INSTALL=$HADOOP_HOME
    export HADOOP_MAPRED_HOME=$HADOOP_HOME
    export HADOOP_COMMON_HOME=$HADOOP_HOME
    export HADOOP_HDFS_HOME=$HADOOP_HOME
    export YARN_HOME=$HADOOP_HOME
    export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
    export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
    export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/nativ"
    export HDFS_NAMENODE_USER="root"
    export HDFS_DATANODE_USER="root"
    export HDFS_SECONDARYNAMENODE_USER="root"
    export YARN_RESOURCEMANAGER_USER="root"
    export YARN_NODEMANAGER_USER="root"

source ~/.bashrc

cd $HADOOP_HOME/etc/hadoop

nano core-site.xml

    <configuration>
        <property> 
            <name>fs.default.name</name> 
            <value>hdfs://localhost:9000</value> 
        </property>
    </configuration>

nano hdfs-site.xml

    <configuration>

        <property> 
            <name>dfs.replication</name> 
            <value>1</value> 
        </property> 
        <property> 
            <name>dfs.name.dir</name> 
            <value>file:///home/hadoop/hadoopinfra/hdfs/namenode </value> 
        </property> 
        <property> 
            <name>dfs.data.dir</name>
            <value>file:///home/hadoop/hadoopinfra/hdfs/datanode </value > 
        </property>
    
    </configuration>

nano yarn-site.xml

    <configuration>

        <property> 
            <name>yarn.nodemanager.aux-services</name> 
            <value>mapreduce_shuffle</value> 
        </property>
    
    </configuration>

nano mapred-site.xml

    <configuration>

        <property> 
            <name>mapreduce.framework.name</name> 
            <value>yarn</value> 
        </property>

    </configuration>

start-dfs.sh

start-yarn.sh

jps

check everything is running...

hive with derby database metastore

tar zxvf db-derby-10.14.2.0-bin.tar.gz

tar zxvf apache-hive-0.14.0-bin.tar.gz

nano ~/.bashrc

    export HIVE_HOME=/home/hadoop/apache-hive-2.3.8-bin
    export PATH=$PATH:$HIVE_HOME/bin
    export CLASSPATH=$CLASSPATH:$HADOOP_HOME/lib/*:.
    export CLASSPATH=$CLASSPATH:/home/hadoop/hive/lib/*:.
    export DERBY_HOME=/home/hadoop/db-derby-10.14.2.0-bin
    export PATH=$PATH:$DERBY_HOME/bin
    export CLASSPATH=$CLASSPATH:$DERBY_HOME/lib/derby.jar:$DERBY_HOME/lib/derbytools.jar

source ~/.bashrc

mkdir $DERBY_HOME/data

cd $HIVE_HOME/conf

cp hive-default.xml.template hive-site.xml

nano hive-site.xml

    <property>
        <name>javax.jdo.option.ConnectionURL</name>
        <value>jdbc:derby://localhost:1527/metastore_db;create=true </value>
        <description>JDBC connect string for a JDBC metastore </description>
    </property>
     <property>
        <name>system:java.io.tmpdir</name>
        <value>/tmp/hive/java</value>
    </property>
    <property>
        <name>system:user.name</name>
        <value>${user.name}</value>
    </property>


nano jpox.properties

    javax.jdo.PersistenceManagerFactoryClass =

    org.jpox.PersistenceManagerFactoryImpl
    org.jpox.autoCreateSchema = false
    org.jpox.validateTables = false
    org.jpox.validateColumns = false
    org.jpox.validateConstraints = false
    org.jpox.storeManagerType = rdbms
    org.jpox.autoCreateSchema = true
    org.jpox.autoStartMechanismMode = checked
    org.jpox.transactionIsolation = read_committed
    javax.jdo.option.DetachAllOnCommit = true
    javax.jdo.option.NontransactionalRead = true
    javax.jdo.option.ConnectionDriverName = org.apache.derby.jdbc.ClientDriver
    javax.jdo.option.ConnectionURL = jdbc:derby://hadoop1:1527/metastore_db;create = true
    javax.jdo.option.ConnectionUserName = APP
    javax.jdo.option.ConnectionPassword = mine

bin/hive

show tabes;

if metastore error came 

schematool -dbType derby -initSchema

Error FUNCTION NUCLEUS ASCII already exists

mv metastore_db metastore_db.tmp

bin/hive

show tabes;

hive with postgresql metastore

nano hive-site.xml

    <property>
		<name>javax.jdo.option.ConnectionURL</name>
		<value>jdbc:postgresql://localhost:5432/hive_metastore</value>
		<description>metadata is stored in a MySQL server</description>
	</property>
	<property>
		<name>javax.jdo.option.ConnectionDriverName</name>
		<value>org.postgresql.Driver</value>
		<description>MySQL JDBC driver class</description>
	</property>
	<property>
		<name>javax.jdo.option.ConnectionUserName</name>
		<value>postgres</value>
		<description>user name for connecting to mysql server</description>
	</property>
	<property>
		<name>javax.jdo.option.ConnectionPassword</name>
		<value>postgres</value>
		<description>password for connecting to mysql server</description>
	</property>

schematool -dbType postgres -initSchema
